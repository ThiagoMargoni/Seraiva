<script setup lang="ts">
    import { useAuthStore } from '~/stores/auth';
    const { isAuthenticated } = useAuthStore();
</script>

<template>
    <main class="flex flex-row w-screen h-screen">
        <SideMenu></SideMenu>
        <slot></slot>
        <RightMenu v-if="isAuthenticated"></RightMenu>
    </main>
</template>