<template>
  <div class="home">
    <h1>Welcome to the Home Page</h1>
    <HelloWorld />
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue';

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
};
</script>

<style scoped>
.home {
  text-align: center;
  margin-top: 50px;
}
</style>