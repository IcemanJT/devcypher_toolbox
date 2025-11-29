<!-- <script setup lang="ts">

import { ref } from "vue";

const API_URL = "http://localhost:8080";

// Dane z UI
const inputText = ref("");
const selectedAlgorithm = ref("caesar"); // domyślnie
const mode = ref<"encode" | "decode">("encode");
const shiftValue = ref<number | null>(null); // tylko dla Caesar

// ================================
// WALIDACJA DANYCH PRZED WYSŁANIEM
// ================================
function validateRequest() {
  if (!inputText.value.trim()) {
    throw new Error("Input text cannot be empty.");
  }

  if (!["caesar", "atbash", "rot13", "base64"].includes(selectedAlgorithm.value)) {
    throw new Error("Invalid algorithm selected.");
  }

  if (selectedAlgorithm.value === "caesar") {
    if (shiftValue.value === null || shiftValue.value < 1 || shiftValue.value > 25) {
      throw new Error("Shift must be a number from 1 to 25 for Caesar cipher.");
    }
  }
}

// ================================
// REQUEST: POST /encode
// ================================
async function encodeRequest() {
  validateRequest();

  // payload zgodny z OpenAPI
  const payload: any = {
    data: inputText.value,
    method: selectedAlgorithm.value,
  };

  if (selectedAlgorithm.value === "caesar") {
    payload.shift = shiftValue.value;
  }

  const res = await fetch(`${API_URL}/encode`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.error || "Error while encoding.");
  }

  const data = await res.json();
  return data.result;
}

// ================================
// REQUEST: POST /decode
// ================================
async function decodeRequest() {
  validateRequest();

  const payload: any = {
    data: inputText.value,
    method: selectedAlgorithm.value,
  };

  // W decode specyfikacja używa pola "key" zamiast "shift"
  if (selectedAlgorithm.value === "caesar") {
    payload.key = String(shiftValue.value);
  }

  const res = await fetch(`${API_URL}/decode`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.error || "Error while decoding.");
  }

  const data = await res.json();
  return data.result;
}

// ================================
// FUNKCJA WYWOŁYWANA PO KLIKNIĘCIU START
// ================================
export async function start() {
  try {
    let result;

    if (mode.value === "encode") {
      result = await encodeRequest();
    } else {
      result = await decodeRequest();
    }

    alert("Wynik: " + result);
  } catch (err: any) {
    alert("Błąd: " + err.message);
  }
}

export {
  inputText,
  selectedAlgorithm,
  mode,
  shiftValue,
};

</script>

<template>
  <div class="page">
    <h1 class="title">DevCypher Toolbox</h1>

    <!-- Folder selector (tabs styled as folders) -->
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

    <!-- Main folder with textarea -->
    <div class="folder-main">
      <textarea
        v-model="inputText"
        placeholder="Wklej tekst do zakodowania / odkodowania..."
      ></textarea>
    </div>

    <!-- Algorithm selector -->
    <select class="algorithm-select" v-model="selectedAlgorithm">
      <option v-for="alg in algorithms" :key="alg" :value="alg">
        {{ alg }}
      </option>
    </select>

    <button class="start-btn" @click="start">START</button>
  </div>
</template>

<style scoped>
/* ---------------- */
/* GENERAL LAYOUT   */
/* ---------------- */

.page {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px 15px;
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.title {
  text-align: center;
  font-size: clamp(28px, 5vw, 40px);
  margin-bottom: 10px;
  font-weight: bold;
}

/* ---------------- */
/* FOLDER TABS      */
/* ---------------- */

.folder-tabs {
  display: flex;
  justify-content: center;
  position: relative;
  gap: 0;
}

.folder-tab {
  flex: 1;
  max-width: 180px;
  padding: 12px 16px;
  text-align: center;
  background: #e8e8e8;
  border: 2px solid #bcbcbc;
  border-bottom: none;
  cursor: pointer;
  border-radius: 8px 8px 0 0;
  font-weight: 600;
  color: black;
  position: relative;
  z-index: 1;
  box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
  transition: 0.15s ease;
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

/* ---------------- */
/* MAIN FOLDER      */
/* ---------------- */

.folder-main {
  background: #ffeb91;
  border: 2px solid #d1b257;
  border-radius: 0 8px 8px 8px;
  padding: 12px;
  min-height: 260px;
  display: flex;
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

textarea {
  width: 100%;
  height: 40vh;
  min-height: 200px;
  border: none;
  resize: none;
  background: transparent;
  outline: none;
  padding: 10px;
  font-size: clamp(16px, 2vw, 20px);
  color: black;
  line-height: 1.5;
}

/* ---------------- */
/* ALGORITHM SELECT */
/* ---------------- */

.algorithm-select {
  width: 220px;
  padding: 12px;
  font-size: 18px;
  color: black;
  margin: 0 auto;
  border-radius: 6px;
  border: 1px solid #bbb;
  background: white;
}

/* ---------------- */
/* START BUTTON     */
/* ---------------- */

.start-btn {
  padding: 14px 40px;
  font-size: 22px;
  background: #3c89ff;
  color: white;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  width: fit-content;
  margin: 0 auto;
  box-shadow: 0 3px 10px rgba(0,0,0,0.2);
  transition: 0.2s;
}

.start-btn:hover {
  background: #1d65e0;
}

/* ---------------- */
/* RESPONSIVE FIXES */
/* ---------------- */

@media (max-width: 600px) {
  .folder-tab {
    max-width: 140px;
    padding: 10px 14px;
    font-size: 14px;
  }

  .folder-main {
    padding: 10px;
  }

  textarea {
    height: 35vh;
  }
}
</style> -->
