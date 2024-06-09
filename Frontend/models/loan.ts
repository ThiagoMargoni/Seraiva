import type { GetBookLoan } from "./book_loan"

export type GetLoan = {
    loan_id: number,
    date: Date,
    total: number,
    book_loans: Array<GetBookLoan>
}

export type PostLoan = {
    
}