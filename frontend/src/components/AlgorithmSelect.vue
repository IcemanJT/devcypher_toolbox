<script setup lang="ts">
import { selectedAlgorithm } from "../api/conversions";

const algorithms = ["caesar", "atbash", "rot13", "base64"];
</script>

<template>
  <select v-model="selectedAlgorithm" class="algorithm-select">
    <option v-for="alg in algorithms" :key="alg" :value="alg">
      {{ alg }}
    </option>
  </select>
</template>

<style scoped>
.algorithm-select {
  width: 220px;
  padding: 12px;
  margin: 0 auto;
  border-radius: 6px;
  border: 1px solid #bbb;
  font-size: 18px;
}
</style>
