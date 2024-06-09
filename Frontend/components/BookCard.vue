<script setup lang="ts">
    import type { GetBook } from '~/models/book';
    import { useAuthStore } from '~/stores/auth';
    import { useCartStore } from '~/stores/cart';

    const { addToCart } = useCartStore();
    const { hasPermission } = useAuthStore();

    type propType = {
        book: GetBook
    };

    const props = defineProps<propType>();
    
    const addItemCart = () => addToCart(props.book);

    const showModal = ref(false);
</script>

<template>
    <div class="flex flex-col items-center justify-evenly ml-[10px]" >
        <img :src="props.book.book_cover" :alt="`Book ${props.book.title} Image`" class="w-[120px] h-[200px] rounded-lg">
        <span class="text-[15px] font-semibold mt-[5px] mb-[5px]">{{ props.book.title }}</span>
        <div class="flex flex-row">
            <Button class="bg-black text-white w-[80px] rounded-[5px]" @click="showModal = true">{{ book.quantity > 0 ? 'Details' : 'Not Available' }}</Button>
            <Button v-if="hasPermission('User') && book.quantity > 0" class="bg-pink-default text-white ml-[5px] rounded-lg w-[24px] h-[24px] flex items-center justify-center" @click="addItemCart">
                <Icon name="material-symbols:add-shopping-cart"></Icon>
            </Button>
        </div>
        <BookModal :book="book" v-if="showModal" @close-modal="showModal = false"></BookModal>
    </div>
</template>