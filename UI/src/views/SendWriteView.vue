<template>
    <div class="bg-white h-screen">
     
        <div class="flex">  
            <SideMenu/>
  
                <div class="mail-box m-3 rounded-2xl flex">
        
                    <AllMail>送信済み</AllMail> 
                    <WriteView/>
                    
                </div>
        </div>  
    </div>
  
  </template>
  
  <script setup>
  
  import SideMenu from '@/components/SideMenu.vue';
  import AllMail from '@/components/AllMail.vue';
  import WriteView from '@/components/WriteView.vue';
  //import NormalView from '@/components/NormalView.vue';
  
  
  
</script>
  
  
<style lang="scss">
  
  .mail-box {
  width: 90%;
  height: 799px;
  background: #F4F4F3;
  }
  
  
</style>