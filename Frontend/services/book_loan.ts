import type { GetBookLoan } from "~/models/book_loan";
import type { Pagination } from "~/models/pagination";
import { BACKEND_URL } from "~/models/url";

export const getUserCurrentBookLoans = async (): Promise<Pagination<GetBookLoan> | null> => {
  return useFetch<Pagination<GetBookLoan>>(`${BACKEND_URL}/book_loan/`)
    .then((res) => {
      return Promise.resolve(res.data.value);
    })
    .catch((error) => {
      console.log("error", error);
      return Promise.reject(null);
    });
};
