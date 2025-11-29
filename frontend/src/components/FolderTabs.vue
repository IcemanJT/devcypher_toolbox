<script setup lang="ts">
import { mode } from "../api/conversions";
</script>

<template>
  <div class="folder-tabs">
    <div
      class="folder-tab decode"
      :class="{ active: mode === 'decode' }"
      @click="mode = 'decode'"
    >
      Decode
    </div>

    <div
      class="folder-tab encode"
      :class="{ active: mode === 'encode' }"
      @click="mode = 'encode'"
    >
      Encode
    </div>
  </div>
</template>

<style scoped>
.folder-tabs {
  display: flex;
  justify-content: center;
  position: relative;
}

.folder-tab {
  flex: 1;
  max-width: 180px;
  padding: 12px;
  text-align: center;
  background: #e8e8e8;
  border: 2px solid #bcbcbc;
  border-bottom: none;
  cursor: pointer;
  border-radius: 8px 8px 0 0;
  font-weight: bold;
  position: relative;
  transition: 0.2s;
  color: black;
}

.folder-tab.decode {
  transform: translateX(12px);
}

.folder-tab.encode {
  transform: translateX(-12px);
}

.folder-tab.active {
  background: #fff7c9;
  border-color: #c9b35a;
  z-index: 3;
  box-shadow: 0 -2px 10px rgba(0,0,0,0.25);
}
</style>
