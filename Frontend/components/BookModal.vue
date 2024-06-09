<script setup lang="ts">
    import type { GetBook } from '~/models/book';

    type propType = {
        book: GetBook
    };

    const props = defineProps<propType>();
</script>

<template>
    <div class="fixed top-0 bottom-0 left-0 right-0 flex justify-center items-center bg-gray-modal z-10">
        <div class="h-[90%] w-1/2 bg-beige rounded-xl">
            <div class="w-full flex justify-between items-center p-3">
                <span class="text-[25px] font-bold">{{ props.book.title }}</span>
                <Icon class="text-[35px] cursor-pointer" name="material-symbols:close-rounded" @click="$emit('close-modal')"></Icon>
            </div>

            <hr class="ml-3 mr-3 border-pink-default">

            <div class="flex flex-col overflow-y-auto items-center max-h-[92%] w-full p-3">
                <div class="flex flex-row">
                    <img :src="props.book.book_cover" :alt="`${props.book.title} Cover`" class="w-[400px] h-auto mt-[3%]">

                    <div class="flex flex-col justify-center">
                        <div v-for="book_image, index in props.book.book_images" class="p-3">
                            <img :src="book_image.image" :alt="`${props.book.title} Image ${index}`" class="w-[100px]">
                        </div>
                    </div>
                </div>

                <div class="py-4 flex flex-col">
                    <span class="text-[35px]">${{ props.book.price }}</span>
                    <span class="text-[25px] text-gray-emote">Remaining Items: {{ props.book.quantity }}</span>

                    <div class="flex flex-row w-full items-center justify-center mt-6">
                        <div v-for="gender in props.book.genders" class="ml-4 bg-pink-default rounded-lg">
                            <span class="p-3 text-white">{{ gender.gender_name }}</span>
                        </div>
                    </div>

                    <div class="mt-6 flex flex-col justify-center items-center">
                        <span class="text-[20px]">More Infos</span>

                        <div class="flex flex-row justify-between min-w-[320px]">
                            <span>Number Pages: {{ props.book.number_pages }}</span> |
                            <span>Publication Year: {{ props.book.publication_year }}</span>
                        </div>

                        <div class="flex flex-row justify-between min-w-[220px]">
                            <span>Volume: {{ props.book.volume }}</span> |  
                            <span>Formart: {{ props.book.format }}</span>
                        </div>
                        
                        <span class="text-[20px] mt-5">Description</span>
                        <span class="w-[300px]">{{ props.book.description }}</span>
                        
                        <span class="text-[20px] mt-5 mb-2">Atuhors</span>
                        <AuthorCard :key="props.book.author_id.author_id" :author="props.book.author_id"></AuthorCard>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
