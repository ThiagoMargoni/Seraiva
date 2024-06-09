export type GetAuthor = {
    author_id: number,
    user_id: number,
    image: string,
    biography: string,
    nickname: string
}

export type PostAuthor = {
    author_id: number,
    user_id: number,
    image: File,
    biography: string,
    nickname: string
}