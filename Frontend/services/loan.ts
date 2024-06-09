import { BACKEND_URL } from "~/models/url";
import { useAuthStore } from "~/stores/auth";
import type { CreateLoan } from "~/stores/cart";

export const saveLoan = async (
  loan: CreateLoan
): Promise<CreateLoan | null> => {
  const { userToken } = useAuthStore();

  const { error, data } = await useFetch<CreateLoan>(`${BACKEND_URL}/loan/`, {
    method: "POST",
    body: loan,
    headers: { Authorization: `${userToken}` },
  });

  if (error.value) {
    console.log("error: ", error.value);
    return Promise.reject(null);
  }

  return Promise.resolve(data.value);
};
