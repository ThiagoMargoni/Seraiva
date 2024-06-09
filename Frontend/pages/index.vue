<script setup lang="ts">
    import type { GetAuthor } from '~/models/author';
    import type { GetBook } from '~/models/book';
    import { getAuthors } from '~/services/author';
    import { getBooks } from '~/services/book';

    const books: Ref<Array<GetBook>> = ref([]);
    const authors: Ref<Array<GetAuthor>> = ref([]);

    const refreshBooks = () => {
        getBooks().then((findBooks) => {
            books.value = findBooks?.results.slice(0, 5) ?? [];
        });
    };

    const refreshAuthor = () => {
        getAuthors().then((findAuthors) => {
            authors.value = findAuthors?.results.slice(0, 6) ?? [];
        });
    }

    refreshBooks();
    refreshAuthor();
</script>

<template>
    <div class="ml-[5vw] flex flex-col justify-center">
        
        <div class="w-[45vw] h-[50px] bg-gray-search_bar_bg rounded-xl mb-6 p-5 flex justify-between items-center cursor-text">
            <!-- Transform into component -->   
            <span class="text-[20px] text-gray-search_bar_font">Type to Search</span>
            <Icon name="mdi:magnify" class="text-pink-default text-[30px]"></Icon>
        </div>

        <div class="w-[45vw] h-[300px] bg-pink-default rounded-xl mb-6">
            <!-- SLIDER -->
            <!-- Transform into component -->
        </div>

        <div class="w-[45vw] mb-10">
            <div class="flex flex-row justify-between">
                <span class="font-bold text-[20px]">All Books</span>
                <div class="text-pink-default underline cursor-pointer">
                    <span class="text-[15px]">See more </span>
                    <Icon class="text-[10px]" name="material-symbols:arrow-forward-ios-rounded"></Icon>
                </div>
            </div>

            <div class="flex flex-row justify-start text-center p-2">
                <div v-for="book in books">
                    <BookCard :key="book.book_id" :book="book"></BookCard>
                </div>
            </div>
        </div>

        <div class="w-[45vw] mb-6">
            <div class="flex flex-row justify-between">
                <span class="font-bold text-[20px]">All Authors</span>
                <div class="text-pink-default underline cursor-pointer">
                    <span class="text-[15px]">See more </span>
                    <Icon class="text-[10px]" name="material-symbols:arrow-forward-ios-rounded"></Icon>
                </div>
            </div>

            <div class="flex flex-row justify-start text-center p-2">
                <div v-for="author in authors" >
                    <AuthorCard :key="author.author_id" :author="author"></AuthorCard>
                </div>
            </div>
        </div>

        <div class="flex flex-row">
            <!-- Transform into component -->
            <div class="bg-white w-[30%] h-[100px] ml-[3%] rounded-lg">

            </div>

            <div class="bg-white w-[30%] h-[100px] ml-[3%] rounded-lg">

            </div>

            <div class="bg-white w-[30%] h-[100px] ml-[3%] rounded-lg">

            </div>
        </div>
    </div>
</template>