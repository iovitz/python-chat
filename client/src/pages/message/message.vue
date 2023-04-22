<template>
	<!-- <EmptyStatus type="message"></EmptyStatus> -->
	<uni-list :border="true">
		<uni-list-chat
			title="uni-app"
			avatar="https://web-assets.dcloud.net.cn/unidoc/zh/unicloudlogo.png"
			note="您收到一条新的消息"
			time="2020-02-02 20:20"
			badge-positon="left"
			badge-text="99"
			@tap="handleGoChat"
			clickable
		></uni-list-chat>
	</uni-list>
</template>

<script setup lang="ts">
// import EmptyStatus from '@/comps/empty-status/empty-status.vue';

const handleGoChat = () => {
	uni.navigateTo({
		url: '/pages/chat/chat',
	});
};
</script>

<style lang="scss" scoped></style>
