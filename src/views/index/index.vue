<template>
	<div>
		<h1>count: {{ count }}</h1>
		<p
			v-for="person in personList"
			:key="person.id"
		>
			{{ person.name }}，{{ person.age }}
		</p>
		<br />
		<button @click="increment">increment</button>
	</div>
</template>

<script lang="ts" setup name="index">
	import { ref } from 'vue';
	import { type Persons } from './index.ts';

	const count = ref(0);
	const increment = () => {
		count.value++;
	};

	let personList: Persons = [
		{ id: 'asyud7asfd01', name: '李四', age: 52 },
		{ id: 'asyud7asfd02', name: '李四', age: 18 },
		{ id: 'asyud7asfd03', name: '王五', age: 5 },
	];
</script>
