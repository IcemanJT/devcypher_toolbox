<script setup lang="ts">
import { inputText } from "../api/conversions";
</script>

<template>
  <div class="folder-main">
    <textarea
      v-model="inputText"
      placeholder="Wklej tekst do zakodowania / odkodowania..."
    ></textarea>
  </div>
</template>

<style scoped>
.folder-main {
  background: #ffeb91;
  border: 2px solid #d1b257;
  border-radius: 0 8px 8px 8px;
  padding: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
  min-height: 260px;
}

textarea {
  width: 100%;
  height: 40vh;
  border: none;
  background: transparent;
  outline: none;
  resize: none;
  font-size: clamp(16px,2vw,20px);
  color: black;
}
</style>
