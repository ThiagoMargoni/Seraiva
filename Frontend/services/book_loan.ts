import type { GetBookLoan } from "~/models/book_loan";
import type { Pagination } from "~/models/pagination";
import { BACKEND_URL } from "~/models/url";
import { useAuthStore } from "~/stores/auth";

export const getUserCurrentBookLoans = async (): Promise<Pagination<GetBookLoan> | null> => {
  const { userToken } = useAuthStore();

  const { error, data } = useFetch<Pagination<GetBookLoan>>(`${BACKEND_URL}/book_loan/`, { headers: { 'Authorization': `${userToken}` } });
    
  if(error.value){
    console.log("error: ", error.value);
    return Promise.reject(null);
  }
  
  return Promise.resolve(data.value);
};

export const getAllNotReturnedBooks = async (): Promise<Pagination<GetBookLoan> | null> => {
  const { userToken } = useAuthStore();

  const { error, data } = useFetch<Pagination<GetBookLoan>>(`${BACKEND_URL}/book_loan/get_all_not_returned/`, { headers: { 'Authorization': `${userToken}` } });
    
  if(error.value){
    console.log("error: ", error.value);
    return Promise.reject(null);
  }
  
  return Promise.resolve(data.value);
} 

export const returnBook = async (book_loan_id: number, date: string): Promise<Pagination<GetBookLoan> | null> => {
  const { userToken } = useAuthStore();

  const { error, data } = useFetch<Pagination<GetBookLoan>>(`${BACKEND_URL}/book_loan/return_book/${book_loan_id}/${date}/`, 
    { headers: { 'Authorization': `${userToken}` } })
    
  if(error.value){
    console.log("error: ", error.value);
    return Promise.reject(null);
  }
  
  return Promise.resolve(data.value);
} 