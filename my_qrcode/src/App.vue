<template>
  <div class="app">
    <n-menu :options="menuOptions" class="menu"/>
    <hr>
    <!-- <n-menu :options="menuOptions"/> -->
    <RouterView class="view"></RouterView>
  </div>
</template>



<script lang="ts">
  import {RouterView,RouterLink} from 'vue-router'
  import type { MenuOption } from 'naive-ui'
  import type { Component } from 'vue'
  import {
    BookOutline as BookIcon,
    HomeOutline as HomeIcon,
    PersonOutline as PersonIcon,
    WineOutline as WineIcon
  } from '@vicons/ionicons5'
  import { NIcon,NMenu } from 'naive-ui'
  import {h} from 'vue'
  export default {
    name:'app'
  }

</script>

<script setup lang="ts">


function renderIcon(icon: Component) {
  return () => h(NIcon, null, { default: () => h(icon) })
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
      ),
    key: 'Text2code',
    icon: renderIcon(HomeIcon)
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
      ),
    key: 'Image2code',
    icon: renderIcon(HomeIcon)
  },

  
]



</script>



<style scoped>
  .app{
    height:700px;
    display: flex;
    justify-content: flex-start;
  }
  .menu{
    height: 100%;
    width: 7%;
  }
  .view{
    width: 93%;
    height: 100%;
    display: flex;
    justify-content: space-around;
    align-items:center;
  }
</style>
