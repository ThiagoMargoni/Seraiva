import type { GetBook } from "~/models/book";
import type { Pagination } from "~/models/pagination";
import { BACKEND_URL } from "~/models/url";

export const getBooks = async (
  pageNumber: number = 0
): Promise<Pagination<GetBook> | null> => {
  return useFetch<Pagination<GetBook>>(`${BACKEND_URL}/book?page=${pageNumber}`)
    .then((res) => {
      return Promise.resolve(res.data.value);
    })
    .catch((error) => {
      console.log("error", error);
      return Promise.reject(null);
    });
};

export const getBook = async (bookId: string): Promise<GetBook | null> => {
  return useFetch<GetBook>(`${BACKEND_URL}/book/${bookId}/`)
    .then((res) => {
      return Promise.resolve(res.data.value);
    })
    .catch((error) => {
      console.log("error", error);
      return Promise.reject(null);
    });
};
