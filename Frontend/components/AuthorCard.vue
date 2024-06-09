<script setup lang="ts">
    import type { GetAuthor } from '~/models/author';

    type propType = {
        author: GetAuthor,
    };

    const props = defineProps<propType>();

    const showModal = ref(false);
</script>

<template>
    <div class="flex flex-col items-center ml-[10px]">
        <img :src="props.author.image" :alt="`${props.author.nickname} Image`" class="w-[50px] h-[50px] rounded-full border-pink-default border-[2px] cursor-pointer" @click="showModal = true">
        <span class="text-[15px] font-semibold cursor-pointer" @click="showModal = true">{{ props.author.nickname }}</span>
        <AuthorModal :author="props.author" v-if="showModal" @close-modal="showModal = false"></AuthorModal>
    </div>
</template>