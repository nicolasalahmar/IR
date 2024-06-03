//@Third Party
import Axios from "axios";
import toast from "react-hot-toast";

//@Dev

// # Initiate axios instance
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

const axiosInstance = Axios.create({ baseURL: API_BASE_URL });

// # base query function
export async function baseQuery(
  {
    url,
    method = "GET",
    body = {},
    params = {},
    headers = {
      "Content-Type": "Application/json",
    },
    hideToast = false,
    hideSuccessToast = false,
  },
  { dispatch, getState, signal }
) {
  try {
    const response = await axiosInstance({
      url,
      data: body,
      method,
      params,
      headers: {
        ...headers,
      },
      signal: signal,
    });

    // # show toast when success
    if (!hideToast && !hideSuccessToast) {
      toast.success(response.data.message ? response.data.message : "Success", {
        id: "SUCCESS",
      });
    }

    return { data: response?.data };
  } catch (error) {
    if (!hideToast) {
      switch (error.code) {
        case "ERR_NETWORK": {
          toast.error(error?.message, { id: "ERR_NETWORK" });
          break;
        }
        case "ERR_CANCELED": {
          toast.error(error?.message, { id: "ERR_CANCELED" });
          break;
        }
        default:
          toast.error(
            error?.response?.data?.message
              ? error.response.data.message
              : "The server encountered an unexpected problem",
            { id: "ERROR" }
          );
          break;
      }
    }

    return {
      error: error?.response?.data
        ? {
            ...error.response.data,
            status: error.response.status,
            server: true,
          }
        : {
            message: "The server encountered an unexpected problem",
            server: true,
          },
    };
  }
}
