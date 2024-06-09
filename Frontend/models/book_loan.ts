import type { GetBook } from './book';

export enum STATUS {
    returned = 'returned',
    delayed = 'delayed',
    borrowed = 'borrowed',
}

export type GetBookLoan = {
    book_id: GetBook,
    devoluption_date: Date,
    real_devoluption_date?: Date,
    status: STATUS
}

export type PostBookLoan = {
    
}