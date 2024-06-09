import { defineStore } from "pinia";
import type { GetBook } from "~/models/book";
import { toast } from 'vue3-toastify';
import { getUserCurrentBookLoans } from "~/services/book_loan";
import { STATUS } from "~/models/book_loan";

export type BookLoan = {
    book_id: number,
    status: string
}

export type CreateLoan = {
    total: number,
    book_loans: Array<BookLoan>
}

export type Cart = {
    books: Array<GetBook>;    
}

export const useCartStore = defineStore('useCartStore', {
    state: (): Cart => ({
        books: []
    }),
    actions: {
      async addToCart(newBook: GetBook){
            const bookAlreadyOnCart = this.getBookIndex(newBook);
            const booksWithUser = await this.getBooksWithUser();
            const userHaveBook = await this.getUserHaveBook(newBook);
            const userHasDelayedBooks = await this.getUserHasDelayedBooks();

            if(!userHasDelayedBooks) {
                if(!userHaveBook) {
                    if(booksWithUser + this.books.length < 3 || this.books.length < 3){

                        if(bookAlreadyOnCart === -1) {
                            this.books.push(newBook);
            
                            toast(`Book successfully added to cart`, {
                                theme: 'light',
                                type: 'success',
                                transition: 'slide',
                                dangerouslyHTMLString: true,
                                autoClose: 2000
                            });
                        } else {
                            toast(`This book is already on the cart`, {
                                theme: 'light',
                                type: 'error',
                                transition: 'slide',
                                dangerouslyHTMLString: true,
                                autoClose: 2000
                            });
                        }
                    }
                    else{
                        toast(`You can have only 3 books at same time`, {
                            theme: 'light',
                            type: 'error',
                            transition: 'slide',
                            dangerouslyHTMLString: true,
                            autoClose: 2000
                        });
                    }
                } else {
                    toast(`You already have this book`, {
                        theme: 'light',
                        type: 'error',
                        transition: 'slide',
                        dangerouslyHTMLString: true,
                        autoClose: 2000
                    });
                }
            } else {
                toast(`You have delayed books. Please return then before getting another`, {
                    theme: 'light',
                    type: 'error',
                    transition: 'slide',
                    dangerouslyHTMLString: true,
                    autoClose: 2000
                });
            }
      },
      removeFromCart(book: GetBook){
        const indexOnCart = this.getBookIndex(book);
        this.books.splice(indexOnCart, 1);
      },
      clearCart(){
        this.books = [];
      }
    },
    getters: {
        getBookIndex: (cart: Cart) => (book: GetBook)=> {
            return cart.books.findIndex(cartBook => cartBook.book_id === book.book_id);
        },
        getCart: (cart: Cart) => () : Array<GetBook> => {
            return cart.books;
        },
        getTotalCart: (cart: Cart): number => {
            return cart.books.reduce((sum, book) => sum += book.price, 0);
        },
        getBooksWithUser: () => async (): Promise<number> => {
            return await getUserCurrentBookLoans().then(data => data?.results.length ?? 0);
        },
        getUserHasDelayedBooks: () => async (): Promise<boolean> => {
            return await getUserCurrentBookLoans().then(data => data?.results.some(loan => loan.status === STATUS.delayed) ?? false)
        },
        getUserHaveBook: () => async (book: GetBook): Promise<boolean> => {
            return await getUserCurrentBookLoans().then(data => data?.results.some(loan => loan.book_id.book_id === book.book_id) ?? false)
        },
        returnCreateLoanObj: (cart: Cart) => (): CreateLoan => {
            return {
                total: cart.books.reduce((sum, book) => sum + book.price, 0),
                book_loans: cart.books.map(book => ({
                    book_id: book.book_id,
                    status: 'borrowed'
                }))
            };
        }
    },
    persist: true
})