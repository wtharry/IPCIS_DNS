<template>
	<div>
		<div class="label">域名基本信息</div>
	    <Table stripe :loading="localLoading" :columns="staticCol" :data="staticInfo"></Table>
	    <hr color="#f5f7f9"/>
	    <div class="label">域名解析IP信息</div>
	    <Table stripe :loading="localLoading" :columns="ipCol" :data="ipInfo"></Table>
	    <hr color="#f5f7f9"/>
	    <div class="label">域名归属信息</div>
	    <Table stripe :loading="remoteLoading" :columns="whoisCol" :data="whoisInfo"></Table>
	</div>
</template>

<script>
	export default {
		data () {
			return {
				targetDomain: "ns2.hostkey.com",
				localLoading: false,
				remoteLoading: false,
	            staticCol: [
	                {
	                    title: "是否DGA",
	                    key: "is_dga"
	                },
	                {
	                    title: "生存时间（TTL）",
	                    key: "ttl"
	                },
	                {
	                    title: "信誉分数",
	                    key: "credit"
	                }
	            ],
	            whoisCol: [
	                {
	                    title: "注册人",
	                    key: "registrar"
	                },
	                {
	                    title: "注册机构",
	                    key: "registrant"
	                },
	                {
	                    title: "注册机构地址",
	                    key: "address"
	                },
	                {
	                    title: "E-Mail",
	                    key: "email"
	                },
	                {
	                    title: "注册时间",
	                    key: "register_date"
	                },
	                {
	                    title: "失效时间",
	                    key: "expire_date"
	                }
	            ],
	            ipCol: [
	                {
	                    title: "解析IP地址",
	                    key: "ip"
	                },
	                {
	                    title: "IP地理位置",
	                    key: "location"
	                },
	                {
	                    title: "IP活动量",
	                    key: "count"
	                }
	            ]
	        }
		},

		mounted () {
			// this.targetDomain = this.$route.params.domain_name
			this.localLoading = true
			this.remoteLoading = true

			this.axios.post("http://118.89.140.118:8888/info/local", 
				JSON.stringify({domain_name: this.targetDomain}))
				.then((response) => {
					this.localLoading = false
					this.staticInfo = [response.data.result.static]
					this.ipInfo = response.data.result.ip
				})
				.catch((response) => {
					this.localLoading = false
					this.$Message.error("对方不想说话，所以等会再试吧");
				})
			this.axios.post("http://118.89.140.118:8888/info/remote", 
				JSON.stringify({domain_name: this.targetDomain}))
				.then((response) => {
					this.remoteLoading = false
					this.whoisInfo = [response.data.result.whois]
				})
				.catch((response) => {
					this.remoteLoading = false
					this.$Message.error("对方不想说话，所以等会再试吧");
				})
		}
	}
</script>

<style scoped>
hr{
	margin: 10px 0;
	background-color: #f5f7f9;
}
.label{
    margin: 10px;
    font-size: 16px;
}
</style>