import { ref } from "vue";

const API_URL = "http://localhost:8080";

// reactive state
const inputText = ref("");
const selectedAlgorithm = ref("caesar");
const mode = ref<"encode" | "decode">("encode");
const shiftValue = ref<number | null>(null);

function validateRequest() {
  if (!inputText.value.trim()) {
    throw new Error("Input text cannot be empty.");
  }

  if (!["caesar", "atbash", "rot13", "base64"].includes(selectedAlgorithm.value)) {
    throw new Error("Invalid algorithm selected.");
  }

  if (selectedAlgorithm.value === "caesar") {
    if (shiftValue.value === null || shiftValue.value < 1 || shiftValue.value > 25) {
      throw new Error("Shift must be a number from 1 to 25.");
    }
  }
}

async function encodeRequest() {
  validateRequest();

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

  return (await res.json()).result;
}

async function decodeRequest() {
  validateRequest();

  const payload: any = {
    data: inputText.value,
    method: selectedAlgorithm.value,
  };

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

  return (await res.json()).result;
}

export async function start() {
  return mode.value === "encode"
    ? encodeRequest()
    : decodeRequest();
}

export {
  inputText,
  selectedAlgorithm,
  shiftValue,
  mode,
};
