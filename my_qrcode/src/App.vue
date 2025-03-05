<template>
  <div class="app">
    <n-menu :options="menuOptions" class="menu" />
    <hr>
    <RouterView class="view"></RouterView>
  </div>
</template>

<script lang="ts">
import { RouterView, RouterLink } from 'vue-router';
import type { MenuOption } from 'naive-ui';
import type { Component } from 'vue';
import {
  TextOutline as TextIcon,
  ImageOutline as ImageIcon
} from '@vicons/ionicons5';
import { NIcon, NMenu } from 'naive-ui';
import { h } from 'vue';

export default {
  name: 'app'
}
</script>

<script setup lang="ts">

function renderIcon(icon: Component) {
  return () => h(NIcon, null, { default: () => h(icon) });
}

const menuOptions: MenuOption[] = [
  {
    label: () =>
      h(
        RouterLink,
        {
          to: {
            name: 'Text',
          }
        },
        { default: () => '文本' }
      ),
    key: 'Text2code',
    icon: renderIcon(TextIcon)
  },
  {
    label: () =>
      h(
        RouterLink,
        {
          to: {
            name: 'Image',
          }
        },
        { default: () => '图片' }
      ),
    key: 'Image2code',
    icon: renderIcon(ImageIcon)
  },
];

</script>

<style scoped>
.app {
  height: 100vh; 
  display: flex;
  justify-content: flex-start;
  background-color: #f5f5f5; 
}

.menu {
  height: 100%;
  width: 160px; 
  padding: 0;
  background-color: white; 
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}

.menu .n-menu-item {
  flex: 1; 
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px; 
  padding: 0 20px; 
  margin: 0; 
  border-radius: 0; 
  transition: background-color 0.3s ease, color 0.3s ease; 
}

.menu .n-menu-item:hover {
  background-color: #409eff;
  color: white; 
}

.view {
  width: calc(100% - 160px);
  height: 100%;
  padding: 20px; 
  background-color: white; 
  box-shadow: -2px 0 8px rgba(0, 0, 0, 0.1);
}
</style>