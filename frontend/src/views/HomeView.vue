<template>
  <div class="page">
    <h1 class="title">DevCypher Toolbox</h1>

    <FolderTabs />
    <TextAreaFolder />
    <AlgorithmSelect />
    <StartButton />
  </div>
</template>

<script setup lang="ts">
import FolderTabs from "../components/FolderTabs.vue";
import TextAreaFolder from "../components/TextAreaFolder.vue";
import AlgorithmSelect from "../components/AlgorithmSelect.vue";
import StartButton from "../components/StartButton.vue";
</script>

<style scoped>
.page {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 22px;
  padding: 20px;
}

.title {
  text-align: center;
  font-weight: bold;
  font-size: clamp(28px, 5vw, 40px);
}
</style>
