<script setup lang="ts">
import { STATUS, type GetBookLoan } from '~/models/book_loan';
import { BACKEND_URL } from '~/models/url';

    type propType = {
        book_loan: GetBookLoan
    };

    const props = defineProps<propType>();
</script>

<template>
    <div class="w-[84%] h-[100px] bg-white mb-6 rounded-lg flex flex-row items-center px-1.5">
        <img :src="`${BACKEND_URL}${props.book_loan.book_id.book_cover}`" 
            :alt="`${props.book_loan.book_id.title} Cover`" class="w-[70px] h-[90px] rounded-lg">
        <div class="flex flex-col w-[85%]">
            <div class="flex flex-row px-4 w-full mb-2">
                <span class="text-[18px] font-bold">{{ props.book_loan.book_id.title }}</span>
                <!-- BOOK STARS -->
            </div>
            <div class="flex flex-row px-4 w-full">
                <span>Return Deadline: {{ props.book_loan.devoluption_date }}</span>
            </div>
        </div>
        <div :class="`w-[25px] h-[22px] mr-4 ml-2 rounded-full ${props.book_loan.status === STATUS.borrowed ? 'bg-green' : 'bg-red'}`"></div>
    </div>
</template>