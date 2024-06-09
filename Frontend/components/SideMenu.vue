<script setup lang="ts">
    import { useMenuStore } from '~/stores/menu';
    import { useAuthStore } from '~/stores/auth';
    import { useCartStore } from '~/stores/cart';

    const menuStore = useMenuStore();
    const authStore = useAuthStore();
    const { clearCart } = useCartStore();

    const showChatbotModal = ref(false);
    const showCartModal = ref(false);

    const menuItems = [
        {
            item: 'Home',
            icon: 'material-symbols:home-rounded',
            permission: true,
            redirectTo: '/'
        },
        {
            item: 'ChatBot',
            icon: 'material-symbols:robot-2',
            permission: true,
            action: () => {
                showChatbotModal.value = true;
            }
        },
        {
            item: 'Cart',
            icon: 'material-symbols:shopping-cart',
            permission: authStore.hasPermission('User'),
            action: () => {
                showCartModal.value = true;
            }
        },
        {
            item: 'My Books',
            icon: 'icon-park-solid:bookshelf',
            permission: authStore.hasPermission('User'),
            redirectTo: '/'
        },
        {
            item: 'Be Author',
            icon: 'material-symbols:verified',
            permission: authStore.hasPermission('User'),
            redirectTo: '/'
        },
        {
            item: 'All Users',
            icon: 'ph:users-fill',
            permission: authStore.hasPermission('Admin'),
            redirectTo: '/'
        },
        {
            item: 'Return Book',
            icon: 'ph:books-fill',
            permission: authStore.hasPermission('Librarian'),
            redirectTo: '/'
        },
        {
            item: 'App Books',
            icon: 'ic:baseline-thumbs-up-down',
            permission: authStore.hasPermission('Librarian'),
            redirectTo: '/'
        },
        {
            item: 'Pub Book',
            icon: 'material-symbols:book-2',
            permission: authStore.hasPermission('Author'),
            redirectTo: '/'
        },
        {
            item: 'Log In',
            icon: 'material-symbols:login-rounded',
            permission: !authStore.isAuthenticated,
            redirectTo: '/user/login'
        },
        {
            item: 'Sign Up',
            icon: 'material-symbols:add-box-rounded',
            permission: !authStore.isAuthenticated,
            redirectTo: '/user/signup'
        },
        {
            item: 'Log Out',
            icon: 'material-symbols:logout-rounded',
            permission: authStore.isAuthenticated,
            action: () => {
                clearCart();
                authStore.signOut({ external: true });
            }
        }
    ]
</script>

<template>
    <div :class="`flex flex-col items-start w-[${menuStore.width}vw] min-h-screen bg-black`">
        <div :class="`flex flex-row items-center py-20 px-10 h-[60px]`">
            <h1 v-if="menuStore.isExpanded" class="text-pink-default font-bold text-[25px] mr-14">SERAIVA</h1>
            <i class="pi pi-bars text-[30px] text-pink-default cursor-pointer" @click="menuStore.toggleMenu"></i>
        </div>

        <div class="flex flex-col justify-start px-10">
            <div v-for="menuItem in menuItems" :key=menuItem.item>
                <NuxtLink v-if="menuItem.permission && menuItem.redirectTo" :to="menuItem.redirectTo" class="text-gray-emote flex flex-row items-center w-full mt-8 cursor-pointer h-[37.5px]">
                    <Icon :name="menuItem.icon" class="text-[30px]"/>
                    <span v-if="menuStore.isExpanded" class="text-[25px] font-bold ml-3">{{ menuItem.item }}</span>
                </NuxtLink>
                <div v-else-if="menuItem.permission && menuItem.action" @click="menuItem.action" class="text-gray-emote flex flex-row items-center w-full mt-8 cursor-pointer h-[37.5px]">
                    <Icon :name="menuItem.icon" class="text-[30px]"/>
                    <span v-if="menuStore.isExpanded" class="text-[25px] font-bold ml-3">{{ menuItem.item }}</span>
                </div>
            </div>
        </div>
        <ChatbotModal v-if="showChatbotModal" @close-modal="showChatbotModal = false"></ChatbotModal>
        <CartModal v-if="showCartModal" @close-modal="showCartModal = false"></CartModal>
    </div>
</template>