import type { GetAuthor } from "./author"
import type { GetBookImage } from "./book_image"
import type { Gender } from "./gender"

export enum FORMAT {
    'ebook' = 'ebook',
    'physical' = 'physical',
}

export enum BOOK_STATUS {
    'pending' = 'pending',
    'approved' = 'approved',
    'refused' = 'refused'
}

export type GetBook = {
    book_id: number,
    title: string,
    quantity: number,
    price: number,
    book_cover: string,
    description: string,
    number_pages: number,
    format: FORMAT,
    publication_year: string,
    volume: number,
    status: BOOK_STATUS,
    author_id: GetAuthor,
    genders: Array<Gender>,
    book_images: Array<GetBookImage>
}

export type PostBook = {
    book_id: number,
    title: string,
    quantity: number,
    price: number,
    book_cover: string,
    description: string,
    number_pages: number,
    format: FORMAT,
    publication_year: string,
    volume: number,
    status: BOOK_STATUS,
    author_id: number,
    genders: Array<number>
}