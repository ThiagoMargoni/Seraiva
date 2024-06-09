<script setup lang="ts">
    import { useCartStore, type Cart } from '~/stores/cart';
    import { saveLoan } from '~/services/loan';
    import { toast } from 'vue3-toastify';

    const cartStore = useCartStore();

    definePageMeta({
        middleware: 'auth'
    });

    const clickSaveLoan = async () => {
        const data = await saveLoan(cartStore.returnCreateLoanObj());
        
        if(data) {
            toast(`Your loan was successfully made`, {
                theme: 'light',
                type: 'success',
                transition: 'slide',
                dangerouslyHTMLString: true,
                autoClose: 2000
            });

            cartStore.clearCart();
        } else {
            toast(`Error while saving the loan`, {
                theme: 'light',
                type: 'error',
                transition: 'slide',
                dangerouslyHTMLString: true,
                autoClose: 2000
            });
        }
    }

    function getDatePlus15Days() {
        const currentDate = new Date();
        currentDate.setDate(currentDate.getDate() + 15);

        const year = currentDate.getFullYear();
        const month = String(currentDate.getMonth() + 1).padStart(2, '0'); 
        const day = String(currentDate.getDate()).padStart(2, '0');

        return `${year}-${month}-${day}`;
    }
</script>

<template>
    <div class="fixed top-0 bottom-0 left-0 right-0 flex justify-center items-center bg-gray-modal z-10">
        <div class="h-[70%] w-1/2 bg-beige rounded-xl">
            <div class="w-full flex justify-between items-center p-3">
                <span class="text-[25px] font-bold">🛒 Your Cart</span>
                <Icon class="text-[35px] cursor-pointer" name="material-symbols:close-rounded"
                    @click="$emit('close-modal')"></Icon>
            </div>

            <hr class="ml-3 mr-3 border-pink-default">

            <table v-if="cartStore.getCart().length > 0" class="flex flex-col">
                <thead class="flex flex-col items-center mt-10 p-4">
                    <tr class="w-full flex flex-row justify-evenly bg-black text-white round rounded-lg">
                        <td>Item</td>
                        <td>Cover</td>
                        <td>Title</td>
                        <td>Author</td>
                        <td>Fomart</td>
                        <td>Price</td>
                        <td>Actions</td>
                    </tr>
                </thead>
                <tbody class="flex flex-col items-center p-4">
                    <tr v-for="(booksOnCart, index) in cartStore.getCart()" :key="index" class="w-full flex flex-row justify-evenly items-center
                     bg-pink-default text-white rounded-lg">
                        <td>{{ index + 1 }}</td>
                        <td><img :src="booksOnCart.book_cover" :alt="`${booksOnCart.title} Cover Image`" class="w-[70px] h-[90px] rounded-lg"/></td>
                        <td>{{ booksOnCart.title }}</td>
                        <td>{{ booksOnCart.author_id.nickname }}</td>
                        <td>{{ booksOnCart.format }}</td>
                        <td>${{ booksOnCart.price }}</td>
                        <td>
                            <Button @click="cartStore.removeFromCart(booksOnCart)">
                                <Icon name="material-symbols:delete-rounded"></Icon>
                            </Button>
                        </td>
                    </tr>
                </tbody>
                <tfoot>
                    <tr class="flex flex-col w-full justify-center items-center fixed bottom-[18%] left-0">
                        <th></th>
                        <th></th>
                        <th></th>
                        <th></th>
                        <th></th>
                        <th>Total: ${{ cartStore.getTotalCart }}</th>
                        <th>Devoluption Date: {{ getDatePlus15Days() }}</th>
                        <th class="bg-black text-white w-[6%] rounded-lg mt-3" @click="clickSaveLoan()">
                            <Button class="w-full">
                                Finish Loan
                            </Button>
                        </th>
                    </tr>
                </tfoot>
            </table>
            <div v-else class="w-full h-[70%] text-[30px] flex justify-center items-center font-bold">
                <span>No Items on Cart!</span>
            </div>
        </div>
    </div>
</template>