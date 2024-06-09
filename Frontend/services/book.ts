import type { GetBook } from "~/models/book";
import type { Pagination } from "~/models/pagination";
import { BACKEND_URL } from "~/models/url";

export const getBooks = async (pageNumber: number = 0): Promise<Pagination<GetBook> | null> => {
  const { error, data } = useFetch<Pagination<GetBook>>(`${BACKEND_URL}/book?page=${pageNumber}`)
    
  if(error.value){
    console.log("error: ", error.value);
    return Promise.reject(null);
  }
  
  return Promise.resolve(data.value);
};

export const getBook = async (bookId: string): Promise<GetBook | null> => {
  const { error, data } = useFetch<GetBook>(`${BACKEND_URL}/book/${bookId}/`)
    
  if(error.value){
    console.log("error: ", error.value);
    return Promise.reject(null);
  }
  
  return Promise.resolve(data.value);
};
