import { defineStore } from "pinia";
import type { GetBook } from "~/models/book";
import { toast } from 'vue3-toastify';
import { getUserCurrentBookLoans } from "~/services/book_loan";
import { STATUS } from "~/models/book_loan";

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
            const userHasDelayedBooks = await this.getUserHasDelayedBooks();

            if(!userHasDelayedBooks) {
                if(booksWithUser + this.books.length < 3 || this.books.length < 3){

                    if(bookAlreadyOnCart === -1) {
                        this.books.push(newBook);
        
                        toast(`Book successfully added to cart`, {
                            theme: 'light',
                            type: 'success',
                            transition: 'slide',
                            dangerouslyHTMLString: true
                        });
                    } else {
                        toast(`This book is already on the cart`, {
                            theme: 'light',
                            type: 'error',
                            transition: 'slide',
                            dangerouslyHTMLString: true
                        });
                    }
                }
                else{
                    toast(`You can have only 3 books at same time`, {
                        theme: 'light',
                        type: 'error',
                        transition: 'slide',
                        dangerouslyHTMLString: true
                    });
                }
            } else {
                toast(`You have delayed books. Please return then before getting another`, {
                    theme: 'light',
                    type: 'error',
                    transition: 'slide',
                    dangerouslyHTMLString: true
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
        }
    },
    persist: true
})