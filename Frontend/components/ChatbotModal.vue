<script setup lang="ts">
    
</script>

<template>
    <div class="fixed top-0 bottom-0 left-0 right-0 flex justify-center items-center bg-gray-modal z-10">
        <div class="h-[90%] w-1/2 bg-beige rounded-xl">
            <div class="w-full flex justify-between items-center p-3">
                <span class="text-[25px] font-bold">Talk with our bot</span>
                <Icon class="text-[35px] cursor-pointer" name="material-symbols:close-rounded" @click="$emit('close-modal')"></Icon>
            </div>

            <hr class="ml-3 mr-3 border-pink-default">

            <div class="w-full h-full flex justify-center items-center">
                <iframe width="737" height="600" allow="microphone;" 
                    src="https://console.dialogflow.com/api-client/demo/embedded/fc9dd71d-e5f2-4506-9910-049419541aa6">
                </iframe>
            </div>
        </div>
    </div>
</template>