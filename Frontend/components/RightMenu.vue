<script setup lang="ts">
    import type { GetBookLoan } from '~/models/book_loan';
    import { getUserCurrentBookLoans } from '~/services/book_loan';
    import { useAuthStore } from '~/stores/auth';

    const authStore = useAuthStore();
    const loans: Ref<Array<GetBookLoan>> = ref([]);

    const refreshLoan = () => {
        getUserCurrentBookLoans().then((findBookLoans) => {
            loans.value = findBookLoans?.results ?? [];
        });
    }

    refreshLoan();
</script>

<template>
    <div class="flex flex-col items-start w-[30vw] h-[100vh] bg-gray-default fixed right-0">
        <div class="flex flex-row justify-evenly p-8 w-full">
            <div class="w-[50px] h-[50px] bg-white rounded-full flex justify-center items-center cursor-pointer">
                <Icon name="material-symbols:notifications-unread" class="text-pink-default text-[30px]"></Icon>
            </div>
            <div class="w-[50px] h-[50px] bg-white rounded-full flex justify-center items-center cursor-pointer">
                <Icon name="material-symbols:bookmark-rounded" class="text-pink-default text-[30px]"></Icon>
            </div>
            <div class="w-[50px] h-[50px] bg-white rounded-full flex justify-center items-center cursor-pointer">
                <Icon name="ic:baseline-mark-unread-chat-alt" class="text-pink-default text-[30px]"></Icon>
            </div>
            <div class="h-[50px] w-[56%] bg-white rounded-lg flex justify-between p-4 items-center font-bold cursor-pointer">
                <span>{{ authStore.user?.first_name }} {{ authStore.user?.last_name }}</span>
                <Icon name="material-symbols:keyboard-arrow-down-rounded" class="text-pink-default text-[26px]"></Icon>
            </div>
        </div>
        <div class="flex flex-row justify-center items-center w-full h-[40%]">
            <div class="w-[84%] h-full rounded-lg bg-white">

            </div>
        </div>

        <span class="p-12 font-bold text-[20px]">Books with You</span>
        <div class="flex flex-col justify-start items-center text-center w-full mt-[-10px]">
            <div v-if="loans.length > 0" v-for="loan in loans" class="flex flex-col items-center w-full">
                <BookLoanCard :book_loan="loan"></BookLoanCard>
            </div>
            <span class="text-[18px]" v-else>Your don't have books <br> in the moment!</span>
        </div>
    </div>
</template>