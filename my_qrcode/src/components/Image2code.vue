<template>
    <div class="construction-page">
      <div class="construction-content">
        <n-icon :component="ConstructIcon" size="60" class="construction-icon" />
        <div class="construction-text">施工中，敬请期待</div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import { NIcon } from 'naive-ui';
  import { ConstructOutline as ConstructIcon } from '@vicons/ionicons5';
  
  export default defineComponent({
    name: 'Image2code',
    components: {
      NIcon
    },
    setup() {
      return {
        ConstructIcon
      };
    }
  });
  </script>
  
  <style scoped>
  .construction-page {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f5f5f5; 
  }
  
  .construction-content {
    text-align: center;
  }
  
  .construction-icon {
    color: #999; 
    margin-bottom: 20px;
  }
  
  .construction-text {
    font-size: 20px; 
    color: #666; 
    font-weight: bold; 
  }
  </style>