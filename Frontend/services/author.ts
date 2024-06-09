import type { Pagination } from "~/models/pagination";
import { BACKEND_URL } from "~/models/url";
import type { GetAuthor } from "~/models/author";

export const getAuthors = async (pageNumber: number = 0): Promise<Pagination<GetAuthor> | null> => {
  const { error, data } = useFetch<Pagination<GetAuthor>>(`${BACKEND_URL}/author?page=${pageNumber}`)
    
  if(error.value){
    console.log("error: ", error.value);
    return Promise.reject(null);
  }
  
  return Promise.resolve(data.value);
};

export const getAuthor = async (authorId: string): Promise<GetAuthor | null> => {
  const { error, data } = useFetch<GetAuthor>(`${BACKEND_URL}/author/${authorId}/`)

  if(error.value){
    console.log("error: ", error.value);
    return Promise.reject(null);
  }
  
  return Promise.resolve(data.value);
};
