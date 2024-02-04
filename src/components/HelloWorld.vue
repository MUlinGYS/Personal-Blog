<template>
	<div>{{ msg }}</div>
</template>

<script setup lang="ts">
	// import { ref } from 'vue';

	defineProps<{ msg: string }>();
</script>

<style scoped>
	.read-the-docs {
		color: #888;
	}
</style>
