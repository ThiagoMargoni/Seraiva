import { defineStore } from "pinia";

export const useMenuStore = defineStore('useMenuStore', {
    state: () => ({
        isExpanded: true,
        width: '15'
    }),
    actions: {
        toggleMenu() {
            this.isExpanded = !this.isExpanded;
            this.width = this.isExpanded ? '15' : '10';
        }
    },
    persist: true
});