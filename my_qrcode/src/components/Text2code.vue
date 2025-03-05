<template>
    <div class="body">
        <div class="inputframe">
            <n-input
                v-model:value="value"
                type="text"
                placeholder="请输入内容"
                :loading="loading"
                class="input"
            />
            <n-button type="primary" ghost class="button" @click="getImage">
                生成图片
            </n-button>
        </div>
        <div class="imageframe">
            <img v-if="imageUrl" src="../image/output.png" alt="Generated Image" class="generated-image" />
            <div v-else class="placeholder">
                <div class="image_text">图片内容</div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { ref } from 'vue';
import { NInput, NButton } from 'naive-ui';
import axios from 'axios';

export default {
    name: "Test2code"
}
</script>

<script setup lang="ts">
let value = ref<string | null>(null);
let imageUrl = ref<string | null>(null);
let loading = ref(false);

async function getImage() {
    try {
        loading.value = true;
        let { data } = await axios.get('http://127.0.0.1:8000/', {
            params: {
                text: value.value
            }
        });
        await sleep(1000);
        imageUrl.value = data;
        console.log(data);
    } catch (error) {
        console.error(error);
    } finally {
        loading.value = false;
    }
}

const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));
</script>

<style scoped>
.body {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    background-color: #f5f5f5;
    min-height: 100vh;
}

.inputframe {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    width: 100%;
    max-width: 400px;
}

.input {
    width: 100%;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.button {
    width: 100%;
    border-radius: 8px;
    transition: background-color 0.3s ease;
}

.button:hover {
    background-color: #409eff;
    color: white;
}

.imageframe {
    display: flex;
    margin-top: 30px;
    padding: 20px;
    background-color: white;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 500px;
    text-align: center;
    align-items: center;
    justify-content: center;
}

.generated-image {
    width: 300px; 
    height: 300px; 
    object-fit: cover; 
    border-radius: 8px;
    transition: opacity 0.3s ease;
}

.placeholder {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 300px; 
    height: 300px; 
    color: #999;
    font-size: 18px;
    background-color: #f0f0f0;
    border-radius: 8px;
}
.image_text{
    text-align: center;
}
</style>