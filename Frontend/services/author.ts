import type { Pagination } from "~/models/pagination";
import { BACKEND_URL } from "~/models/url";
import type { GetAuthor } from "~/models/author";

export const getAuthors = async (
  pageNumber: number = 0
): Promise<Pagination<GetAuthor> | null> => {
  return useFetch<Pagination<GetAuthor>>(
    `${BACKEND_URL}/author?page=${pageNumber}`
  )
    .then((res) => {
      return Promise.resolve(res.data.value);
    })
    .catch((error) => {
      console.log("error", error);
      return Promise.reject(null);
    });
};

export const getAuthor = async (
  authorId: string
): Promise<GetAuthor | null> => {
  return useFetch<GetAuthor>(`${BACKEND_URL}/author/${authorId}/`)
    .then((res) => {
      return Promise.resolve(res.data.value);
    })
    .catch((error) => {
      console.log("error", error);
      return Promise.reject(null);
    });
};
