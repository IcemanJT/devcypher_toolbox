<script setup lang="ts">
import { start } from "../api/conversions";
</script>

<template>
  <button class="start-btn" @click="start">START</button>
</template>

<style scoped>
.start-btn {
  padding: 14px 40px;
  font-size: 22px;
  background: #3c89ff;
  color: white;
  border-radius: 10px;
  border: none;
  cursor: pointer;
  margin: 0 auto;
}
</style>
