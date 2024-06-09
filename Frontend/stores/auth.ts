import { defineStore } from "pinia";
import type { User } from "~/models/user";

export const useAuthStore = defineStore('useAuthStore', () => {
  const { data, signOut } = useAuth();

  const user = computed<User | null>(() => {
    if (data.value) {
      return data.value ? (data.value as unknown as User) : null;
    }

    return null;
  });

  const isAuthenticated = computed(() => !!user.value);
  const userRoles = computed(() => user.value?.groups || []);

  function hasPermission(permission: string) {
    return userRoles.value.some(role => role.name === permission);
  }

  return {
    user,
    isAuthenticated,
    userRoles,
    hasPermission,
    signOut
  };
});
