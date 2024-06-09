type Group = {
    id: number,
    name: string
}

export type UserPermission = {
    id: number,
    name: string,
    codename: string
}

export type User = {
    id: number;
    username: string;
    email: string;
    first_name: string;
    last_name: string;
    groups: Array<Group>;
    user_permissions: Array<UserPermission>;
}