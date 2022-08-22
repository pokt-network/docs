function memoizeAsync(fn, getKey) {
  const memo = {},
    progressQueues = {};

  return function memoized(...allArgs) {
    const callback = allArgs[allArgs.length - 1];
    const args = allArgs.slice(0, -1);
    const key = getKey(...args);

    if (memo.hasOwnProperty(key)) {
      callback(key);
      return;
    }

    if (!progressQueues.hasOwnProperty(key)) {
      // processing new key, create an entry for it in progressQueues
      progressQueues[key] = [callback];
    } else {
      // processing a key that's already being processed, enqueue it's callback and exit.
      progressQueues[key].push(callback);
      return;
    }

    fn.call(this, ...args, (data) => {
      // memoize result
      memo[key] = data;
      // process all the enqueued items after it's done
      for (let callback of progressQueues[key]) {
        callback(data);
      }
      // clean up progressQueues
      delete progressQueue[key];
    });
  };
}

const getAPIDocument = async (documentUrl, portalPrefix) => {
  const data = await fetch(documentUrl).then((res) => res.json());
  console.log(data.servers);
  data.servers = [
    {
      url: "https://" + portalPrefix + ".gateway.pokt.network/v1/lb/{PortalID}",
      description: "Pocket Portal",
      variables: {
        PortalID: {
          default: "YourPortalIdHere",
          description:
            "Found after registering an app with the [Pocket Portal](https://www.portal.pokt.network/).",
        },
      },
    },
  ];
  return JSON.stringify(data);
};

function getChains() {
  document.getElementById("chainDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (e) {
  if (!e.target.matches(".dropbtn")) {
    var myDropdown = document.getElementById("chainDropdown");
    if (myDropdown.classList.contains("show")) {
      myDropdown.classList.remove("show");
    }
  }
};
