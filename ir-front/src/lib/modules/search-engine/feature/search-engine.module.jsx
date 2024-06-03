//@Core
import { useState } from "react";

//@Third Party
import toast from "react-hot-toast";
import { useSearchParams } from "react-router-dom";

//@Dev
// # Shared
// ## UI
import {
  EmptyMessage,
  ErrorMessage,
  LoadingIndicator,
  NormalButtonInput,
  NormalTextInput,
} from "@/shared/ui";
// # Locale
// ## Utils
import { SearchIcon } from "../utils";
// ## Services
import { useLazyGetSearchResultBySearchTermQuery } from "../data-access";
// ## UI
import { SearchResultItem } from "../ui/search-result-item/search-result-item";

export function SearchEngineModule() {
  //* @Initiate
  const [searchParams] = useSearchParams();

  //* @Component State
  // # Locale
  const [searchTerm, setSearchTerm] = useState("");

  // # Global
  const selectedDataSet = searchParams.get("dataset");

  //* @Async
  const [
    getSearchResult,
    {
      data: searchResultData = { data: [] },
      error: searchResultError = {},
      isError: isSearchResultError,
      isLoading: isSearchResultLoading,
    },
  ] = useLazyGetSearchResultBySearchTermQuery({
    searchTerm,
    dataset: selectedDataSet.toLowerCase(),
  });

  //* @Handlers
  const handleSearchTermChange = (value) => setSearchTerm(value);

  const handleSearch = async () => {
    try {
      await getSearchResult({
        searchTerm,
        dataset: selectedDataSet.toLowerCase(),
      }).unwrap();
    } catch (error) {
      if (!error.server) {
        toast.error(error.message ?? "Something went wrong");
      }
    }
  };

  //* @Render Search Result
  let searchResultView = <></>;

  if (isSearchResultLoading) {
    searchResultView = (
      <div className="flex gap-3 m-auto">
        <LoadingIndicator />
        <p className="text-lg font-bold text-black">Loading </p>
      </div>
    );
  } else if (isSearchResultError) {
    searchResultView = <ErrorMessage error={searchResultError} />;
  } else if (searchResultData.data.length === 0) {
    searchResultView = <EmptyMessage />;
  } else {
    searchResultView = (
      <div className="flex flex-col gap-4 w-1/2 md:w-full">
        {searchResultData.data
          //.sort(({ rank: rankA }, { rank: rankB }) => rankA - rankB)
          .map((searchResult) => (
            <SearchResultItem key={searchResult.rank} {...searchResult} />
          ))}
      </div>
    );
  }

  return (
    <div className="min-h-screen py-10 flex flex-col items-center gap-11  bg-darkGray-light">
      <div className="flex gap-3 items-end">
        <div className="w-96">
          <NormalTextInput
            type="text"
            name="searchTerm"
            value={searchTerm}
            placeholder="Search..."
            onChange={handleSearchTermChange}
          />
        </div>
        <NormalButtonInput
          label={<SearchIcon />}
          className="h-[47px] w-[45px] bg-white border border-gray"
          onClick={handleSearch}
        />
      </div>
      <div className="w-full flex justify-center">{searchResultView}</div>
    </div>
  );
}
