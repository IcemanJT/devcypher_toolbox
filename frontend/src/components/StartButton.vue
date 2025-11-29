<script setup lang="ts">
import { start } from "../api/conversions";

const handleClick = async () => {
  try {
    const result = await start();
    alert("Wynik: " + result); // or show it somewhere else in the UI
  } catch (err: any) {
    alert("Błąd: " + (err?.message || "Unknown error"));
  }
};
</script>

<template>
  <button class="start-btn" @click="handleClick">START</button>
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
