   <script lang="ts">
    import type { params, paramValues, sharedParams } from "$lib/types";
    export let sharedParam:sharedParams;
    export let processedAxis: params
    export let outputData: paramValues;
    
    

   </script>
   
   <!-- ---------- RIGHT SIDEBAR ---------- -->
    <aside
      id="layout-toggle"
      class="overlay overlay-open:translate-x-0 drawer drawer-end inset-y-0 end-0 hidden [--auto-close:lg] sm:w-1/4 lg:z-50 lg:block lg:translate-x-0 lg:shadow-none"
      aria-label="Sidebar"
      tabindex="-1"
    >
      <div class="drawer-body border-base-content/20 h-full border-e p-6">
        <div class="border-base-content/20 rounded-box skeleton-striped h-full border">
          <div>
            <form action="?/submit_axis" method="post">
            <div class="card sm:max-w-sm">
              <div class="card-body border p-4">
                <h5 class="card-title mb-2.5">Verify Axis</h5>
                <p class="mb-4">Note: Verify view points and boundaries before you submit</p>
                <p class="mb-4">{JSON.stringify(processedAxis, null, 3)}</p>

                <div class="card-actions">
                  <button on:click={()=>{

                  }} class="btn btn-primary self-center">Submit Axis</button>
                </div>
              </div>
            </div>
            </form>

            <div class="card sm:max-w-sm">
              <div class="card-body border p-4">
                <h5 class="card-title mb-2.5">Gnerated Parameters</h5>
                <p class="mb-4">Note: Confirm the output before you register the receipt's axis</p>
                <p class="mb-4">{JSON.stringify(outputData, null, 3)}</p>

                <div class="card-actions">
                  <button on:click={()=>{

                  }} class="btn btn-primary self-center">Register Receipt</button>
                </div>
              </div>
            </div>

            <div class="card sm:max-w-sm">
              <div class="card-body">
                <h5 class="card-title mb-2.5">Receipt Registry  <span>(0)</span></h5>
                <input type="search" class="p-2 border-0 text-white bg-gray-400" />
                <div class="card-actions">
                  <button class="btn btn-primary">Preview</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </aside>
