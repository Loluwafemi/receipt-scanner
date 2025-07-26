<script lang="ts">
    import Lsidebar from "$lib/components/LSIDEBAR.svelte";
    import Main from "$lib/components/Main.svelte";
    import Rsidebar from "$lib/components/RSIDEBAR.svelte";
    import type { paramAxis, params, paramStatus, sharedParams } from "$lib/types";
    


    let sharedParam: sharedParams = {
        status: {
            accountName: false,
            amount: false,
            bankName: false,
            dateTime: false
        },
        file: null,
        areas: null
        
    }

  let isVisible: 'hidden' | "block" = 'hidden'
  let axixValues:params;
  let processedAxis: params

</script>

    <Lsidebar bind:axixValues bind:isVisible bind:sharedParam />

    <div class="flex mx-20 grow flex-col lg:px-75">
        <Main bind:processedAxis bind:axixValues={axixValues} bind:sharedParam />
    </div>
    

    <Rsidebar bind:processedAxis bind:sharedParam />