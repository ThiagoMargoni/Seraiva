from apscheduler.schedulers.background import BackgroundScheduler
from .models import *
from datetime import datetime, timedelta

def StartScheduler():
    scheduler = BackgroundScheduler()
    scheduler.remove_all_jobs()
    scheduler.add_job(EmailJob, 'interval', seconds=43200) # 43200 seconds = 12 hours
    scheduler.start()

def SendMail(subject, body, email):
    print(subject, body, email)

def EmailJob():
    print('Starting Email Job...')

    now = datetime.now().date()

    loans = BookLoan.objects.filter(status__in=['delayed', 'borrowed']).filter(devoluption_date__lte=now+timedelta(days=3))

    for loan in loans:
        
        days_until_devoluption = loan.devoluption_date - now
        body, subject = '', ''
        user_loan = Loan.objects.filter(loan_id=loan.loan_id).first()

        if days_until_devoluption.days in [1, 2, 3]:
            body = f'''<html>
                        <body>
                            <p>Olá, {user_loan.user_id.first_name}! Espero que esteja tudo bem.<br>
                            Esse é um e-mail automático para te lembrar que você deve devolver o livro {loan.book_id.title} no dia {loan.devoluption_date}.<br>
                            Fique atento ao prazo de entrega!
                            </p>
                        </body>
                    </html>'''
            
            subject = 'Prazo de Devolução Próximo'

        elif days_until_devoluption == 0:
            body = f'''<html>
                        <body>
                            <p>Olá, {user_loan.user_id.first_name}! Espero que esteja tudo bem.<br>
                            Esse é um e-mail automático para te lembrar que você deve devolver o livro {loan.book_id.title} hoje!
                            </p>
                        </body>
                    </html>'''
            
            subject = 'Prazo de Devolução Expira Hoje'
        
        else:
            if loan.status != 'delayed':
                loan.status = 'delayed'
                loan.save()

            body = f'''<html>
                        <body>
                            <p>Olá, {user_loan.user_id.first_name}! Espero que esteja tudo bem.<br>
                            Você está com a entrega do livro {loan.book_id.title} atrasada. A cada dia de atraso sua multa aumentará em 2 reais.
                            Atualmente o valor está em {days_until_devoluption.days * -2}. Poupe-nos trabalho e faça a devolução, junto com o pagaemnto da taxa por favor.
                            </p>
                        </body>
                    </html>'''
            
            subject = f'Prazo de Devolução Atrasado em {days_until_devoluption.days} dia(s)'
            
        SendMail(subject=subject, body=body , email=user_loan.user_id.email)