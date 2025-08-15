<script lang="ts">
    import Lsidebar from "$lib/components/LSIDEBAR.svelte";
    import Main from "$lib/components/Main.svelte";
    import Rsidebar from "$lib/components/RSIDEBAR.svelte";
    import type { paramAxis, params, paramStatus, paramValues, sharedParams } from "$lib/types";
    


    let sharedParam: sharedParams = {
        status: {
            accountName: false,
            amount: false,
            bankName: false,
            dateTime: false
        },
        file: null,
        areas: null,
        output: null
        
    }

  let isVisible: 'hidden' | "block" = 'hidden'
  let axixValues:params;
  let processedAxis: params
  let outputData: paramValues;

</script>

    <Lsidebar bind:axixValues bind:isVisible bind:sharedParam />

    <div class="flex mx-20 grow flex-col lg:px-75">
        <Main bind:outputData bind:processedAxis bind:axixValues={axixValues} bind:sharedParam />
    </div>

    <Rsidebar bind:outputData bind:processedAxis bind:sharedParam />