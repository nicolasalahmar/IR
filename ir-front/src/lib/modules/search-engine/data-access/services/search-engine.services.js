//@API Slice
import { apiSlice } from "@/store/api/api.slice";

//@Models
import { searchResultModel } from "../../utils";

const searchEngineApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    //* @QUERY / GET
    getSearchResultBySearchTerm: builder.query({
      query: ({ searchTerm, dataset }) => ({
        url: `/search/${dataset}/${searchTerm}`,
        method: "GET",
        hideSuccessToast: true,
      }),
      transformResponse: (response) => {
        const responseData = response.map((result) =>
          searchResultModel({
            rank: result.rank,
            text: result.text,
            score: result.score,
            docId: result.doc_id,
          })
        );

        return { data: responseData };
      },
    }),
  }),
});

export const { useLazyGetSearchResultBySearchTermQuery } = searchEngineApiSlice;
