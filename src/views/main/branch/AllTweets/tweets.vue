<template>
	<!-- 推荐位 -->
	<div>
		<el-carousel
			height="400px"
			direction="vertical"
			type="card"
			:autoplay="true"
		>
			<el-carousel-item
				v-for="item in 4"
				:key="item"
			>
				<h3
					text="2xl"
					justify="center"
				>
					{{ item }}
				</h3>
			</el-carousel-item>
		</el-carousel>
	</div>
	<div>
		<el-empty description="tweets" />
	</div>
	<el-card shadow="hover">
		<template #header>
			<span>推文 name</span>
		</template>
		<div
			v-for="o in 4"
			:key="o"
			class="text item"
		>
			{{ '内容 ' + o }}
		</div>
		<template #footer>其他content</template>
	</el-card>
</template>

<script setup lang="ts"></script>

<style scoped>
	.el-carousel__item h3 {
		color: #475669;
		opacity: 0.75;
		line-height: 200px;
		margin: 0;
		text-align: center;
	}

	.el-carousel__item:nth-child(2n) {
		background-color: #99a9bf;
	}

	.el-carousel__item:nth-child(2n + 1) {
		background-color: #d3dce6;
	}
</style>
