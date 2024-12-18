<template>
    <div class="body">
        <div class="inputframe">
            <n-input
                v-model:value="value"
                type="text"
                placeholder="基本的 Input"
                :loading="loading"
            />
            <n-button type="primary" ghost class="button" @click="getImage">
                生成
            </n-button>
        </div>
        <div class="imageframe">
            <img v-if="imageUrl" src="../image/output.png" alt="Generated Image" class="generated-image" />
        </div>
    </div>
</template>



<script lang="ts">
    import { ref} from 'vue';
    import { NInput,NButton } from 'naive-ui';
    import  axios  from 'axios';
    export default {
        name:"Test2code"
    } 

</script>

<script setup lang="ts">
    let value=ref(null)
    let text=ref('')
    let imageUrl = ref<string | null>(null)
    let loading=ref(false)

    async function getImage(){

        try {
            let { data } = await axios.get('http://127.0.0.1:8000/', {
                params: {
                    text:value.value 
                }
            });
            loading.value=true
            await sleep(1000)
            loading.value=false
            imageUrl.value = data
            console.log(data)
        } catch (error) {
            const err = error
            console.log(err)
        }

    }
    
    const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

</script>

<style scoped>
    .body{
        display: flex;
        align-items:center;
        align-content: center;
        align-items: center;
    }
    .inputframe{
        display: flex;
        flex-direction: column;
        align-content: center;
        align-items: center;
        width: 30%;
        gap: 30px;
    }
    .button{
        width: 30%;
        align-content: center;
        align-items: center;
    }
    .imageframe {
        display: inline-block; 
        background: linear-gradient(90deg, #333 50%, transparent 0) repeat-x,
                    linear-gradient(90deg, #333 50%, transparent 0) repeat-x,
                    linear-gradient(0deg, #333 50%, transparent 0) repeat-y,
                    linear-gradient(0deg, #333 50%, transparent 0) repeat-y;
        background-size: 10px 2px, 10px 2px, 2px 10px, 2px 10px;
        background-position: 0 0, 0 100%, 0 0, 100% 0;
        padding: 10px;
        width: 310px;
        height: 315.6px;
    }
    .generated-image{
        width: 100%;
    }


</style>