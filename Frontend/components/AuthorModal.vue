<script setup lang="ts">
import type { GetAuthor } from '~/models/author';

    type propType = {
        author: GetAuthor
    };

    const props = defineProps<propType>();
</script>

<template>
    <div class="fixed top-0 bottom-0 left-0 right-0 flex justify-center items-center bg-gray-modal z-10">
        <div class="h-3/4 w-1/2 bg-beige rounded-xl">
            <div class="w-full flex justify-between items-center p-3">
                <span class="text-[25px] font-bold">{{ props.author.nickname }}</span>
                <Icon class="text-[35px] cursor-pointer" name="material-symbols:close-rounded" @click="$emit('close-modal')"></Icon>
            </div>

            <hr class="ml-3 mr-3 border-pink-default">

            <div class="flex flex-col overflow-y-auto items-center max-h-[92%] w-full p-3">
                <div class="flex flex-row">
                    <img :src="props.author.image" :alt="`${props.author.nickname} Cover`" class="w-[400px] h-auto mt-[3%] rounded-full">
                </div>

                <div class="py-4 flex flex-col w-[80%]">
                    <span class="text-[35px]">Biography</span>
                    <span class="text-[25px] text-gray-emote">{{ props.author.biography }}</span>
                </div>
            </div>
        </div>
    </div>
</template>
